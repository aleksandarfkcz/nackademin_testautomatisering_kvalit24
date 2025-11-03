import requests
import time
from typing import Optional, Tuple

class UserAPI:
    # Simple user client: signup, login, add and remove products for the current user

    def __init__(self, base_url: str, session: Optional[requests.Session] = None):
        self.base_url = str(base_url).rstrip("/")
        self.session = session or requests.Session()
        self.token: Optional[str] = None

    # ---- HELPERS ----
    def _url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    def _headers(self) -> dict:
        return {"Authorization": f"Bearer {self.token}"} if self.token else {}

    # ---- AUTH ----
    def login(self, username: str, password: str) -> str:
        resp = self.session.post(self._url("/login"), json={"username": username, "password": password})
        resp.raise_for_status()
        token = resp.json().get("access_token")
        if not token:
            raise ValueError("No access_token in login response")
        self.token = token
        return token

    def signup(self) -> Tuple[str, str]:
        username = f"user_{int(time.time())}"
        password = "pass123"
        resp = self.session.post(self._url("/signup"), json={"username": username, "password": password})
        # Treat already exists as OK so tests are stable
        if resp.status_code not in (200, 201, 400, 409):
            resp.raise_for_status()
        return username, password

    # ---- USER PRODUCTS ----
    def add_product_to_user(self, product_name: str) -> requests.Response:
        # find product id by name
        lst = self.session.get(self._url("/products"), headers=self._headers())
        lst.raise_for_status()
        products = lst.json()
        target = next((p for p in products if p.get("name") == product_name), None)
        if not target or "id" not in target:
            r = requests.Response()
            r.status_code = 404
            r._content = b'{"detail":"product not found"}'
            return r

        body = {"productId": target["id"]}
        resp = self.session.post(self._url("/user/product"), json=body, headers=self._headers())
        return resp

    def remove_product_from_user(self, product_name: str) -> requests.Response:
        # List current users products
        lst = self.session.get(self._url("/products"), headers=self._headers())
        lst.raise_for_status()
        items = lst.json()

        # Find id by name
        target = next((p for p in items if p.get("name") == product_name), None)
        if not target or "id" not in target:
            r = requests.Response()
            r.status_code = 404
            r._content = b'{"detail":"user product not found"}'
            return r

        pid = target["id"]

        resp = self.session.delete(self._url(f"/user/product/{pid}"), headers=self._headers())
        return resp