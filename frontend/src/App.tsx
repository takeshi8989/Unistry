import Header from "./components/Header";
import Home from "./pages/Home";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import School from "./pages/School";
import Event from "./pages/Event";
import Profile from "./pages/Profile";
import Members from "./pages/Members";
import Chat from "./pages/Chat";
import CreateEvent from "./pages/CreateEvent";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
function App() {
  return (
    <div className="h-screen">
      <Header />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/school/:id" element={<School />} />
          <Route path="/event/:id" element={<Event />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/school/members" element={<Members />} />
          <Route path="/chat" element={<Chat />} />
          <Route path="/create" element={<CreateEvent />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
