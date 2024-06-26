import LogIn from "./components/login";
import CreateAccount from "./components/createAccount";
import ForgotPassword from "./components/forgotPassword";
import { Route, Routes, useLocation } from "react-router-dom";
import Home from "./components/Home";
import PasswordReset from "./components/PasswordReset";
import NotFound from "./components/404";
import { ToastContainer } from "react-toastify";
import Send from "./components/sendResetCode";
import { AuthProvider } from "./hooks/authContext";
import Products from "./components/products";
import Cart from "./components/cart";
import ProductDetails from "./components/ProductDetails";
import { CookiesProvider } from "react-cookie";
import About from "./components/about";
import CategoryDetails from "./components/categorydetails";
import Dashboard from "./components/dashboard";
import Navbar from "./common/navbar";

function App() {
  const { pathname } = useLocation();
  const urlsToExclude = [
    "/login",
    "/createAccount",
    "/sendResetCode",
    "/PasswordReset",
    "/forgotPassword",
  ];
  const shouldRender = !urlsToExclude.includes(pathname);
  return (
    <div>
      {shouldRender && <Navbar />}
      <CookiesProvider>
        <AuthProvider>
          <Routes>
            <Route path="*" element={<NotFound />} />
            <Route path="createAccount" element={<CreateAccount />} />
            <Route path="sendResetCode" element={<Send />} />
            <Route path="forgotPassword" element={<ForgotPassword />} />
            <Route path="logIn" element={<LogIn />} />
            <Route path="PasswordReset" element={<PasswordReset />} />
            <Route path="Products" element={<Products />} />
            <Route path="cart" element={<Cart />} />
            <Route path="products/:productId" element={<ProductDetails />} />
            <Route path="category/:vendor" element={<CategoryDetails />} />
            <Route path="/about" element={<About />} />
            <Route path="/" element={<Home />} />
            <Route path="/admin" element={<Dashboard />} />
          </Routes>
        </AuthProvider>
      </CookiesProvider>
      <ToastContainer />
    </div>
  );
}

export default App;
