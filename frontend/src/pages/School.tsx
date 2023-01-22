import React from "react";
import SideEvents from "../components/SideEvents";
import useWindowSize from "../hooks/useWIndowSize";
import { GoLocation } from "react-icons/go";
import { IoPeopleOutline } from "react-icons/io5";
import { SchoolModel } from "../models.ts/School";
import { useParams } from "react-router-dom";
import useFetch from "../hooks/useFetch";

// ten_member_images
const members: number[] = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1];

const School: React.FC = () => {
  const windowSize = useWindowSize();
  const params = useParams();
  const [school, isLoading, error, refetch]: [
    SchoolModel,
    boolean,
    any,
    () => void
  ] = useFetch("/schools/" + params.id + "/");

  if (error) {
    console.log(error);
    refetch();
  }

  return (
    <div className="h-screen w-full flex pt-20 relative z-10">
      {windowSize >= 768 && (
        <div className="w-1/3 h-full">
          <SideEvents title={"Events"} />
        </div>
      )}
      {!isLoading && (
        <div className="md:w-2/3 w-full">
          <div className="flex justify-center mt-10 items-center mb-10">
            <img
              src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOPRtwEAg8NC4x2Sg_E2DFKl9nn3Ku_J7_2g&usqp=CAU"
              alt="logo"
              className="mr-6 w-1/4"
            />
            <h1
              className="text-center"
              style={{ fontSize: Math.floor((windowSize * 100) / 1600) }}
            >
              {school?.name}
            </h1>
          </div>

          <div className="flex justify-center w-full">
            <GoLocation size={30} />
            <span className="text-center text-xl ml-2 mr-6">
              {school?.location}
            </span>
            <IoPeopleOutline size={30} />
            <span className="text-center text-xl mx-2">
              {school?.num_of_members} members
            </span>
          </div>
          <div className="flex justify-center mt-5">
            <button className="border border-2 hover:bg-yellow-100 font-bold border-yellow-500 px-2 py-4 bg-white rounded text-yellow-500 text-2xl mx-4">
              Create a New Event
            </button>
          </div>
          <div className="w-4/5 sm:w-1/2 lg:w-4/5 2xl:w-1/2 mx-auto mt-6">
            <p className="text-center text-xl">Members</p>
            <div className="mt-4 flex justify-center flex-wrap">
              {members.map((member) => (
                <img
                  src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOPRtwEAg8NC4x2Sg_E2DFKl9nn3Ku_J7_2g&usqp=CAU"
                  alt="profile"
                  className="lg:w-28 w-16"
                />
              ))}
            </div>
            <p className="h-28 text-right text-xl mr-2 text-blue-600">
              See all
            </p>
          </div>
          {windowSize < 768 && (
            <div className="">
              <SideEvents title={"Events"} />
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default School;
