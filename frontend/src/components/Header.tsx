import React from "react";
import logo from "../assets/unistry_logo.png";
import { BiMessage } from "react-icons/bi";
import { IoMdNotificationsOutline } from "react-icons/io";
import { CgProfile } from "react-icons/cg";
import { HiBars3 } from "react-icons/hi2";
import useWindowSize from "../hooks/useWIndowSize";

const Header: React.FC = () => {
  const windowSize = useWindowSize();
  return (
    <div className="w-full border flex justify-between bg-white z-50 fixed">
      {windowSize < 768 && (
        <div className="absolute flex justify-center ml-2 mt-5">
          <HiBars3 size={40} />
        </div>
      )}
      <a
        href="http://localhost:3000/"
        className="md:w-1/3 w-full text-orange-600 text-center my-auto flex justify-center items-center"
      >
        <img alt="unistry-logo" className="my-auto" width={250} src={logo} />
      </a>
      {windowSize >= 768 && (
        <div className="w-1/3 flex justify-center my-auto items-center mr-4">
          <div className="m-3 flex flex-col items-center">
            <BiMessage size={35} />
            <p className="text-center">Messages</p>
          </div>
          <div className="m-3 flex flex-col items-center">
            <IoMdNotificationsOutline size={35} />
            <p className="text-center">Notifications</p>
            <div className="absolute bg-orange-600 rounded-full w-4 h-4 my-auto ml-4"></div>
          </div>
          <div className="m-3">
            <CgProfile size={60} />
          </div>
        </div>
      )}
    </div>
  );
};

export default Header;
