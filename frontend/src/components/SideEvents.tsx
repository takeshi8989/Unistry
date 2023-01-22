import React from "react";
import useFetch from "../hooks/useFetch";
import { EventModel } from "../models.ts/Event";
import EventCard from "./EventCard";

const Sidebar: React.FC<{ title: string }> = ({ title }) => {
  let [events, isLoading, error] = useFetch("/events/");

  if (error) {
    events = [];
    console.log(error);
  }

  return (
    <div className="border-x w-full mt-1 flex flex-col items-center">
      <h1 className="text-center text-2xl mt-4 mb-4">{title}</h1>
      <div className="flex justify-center mb-4">
        <button className="border px-2 py-2 bg-yellow-500 rounded text-white text-xl mx-4 lg:w-32 w-20 hover:bg-yellow-600">
          Past
        </button>
        <button className="border border-yellow-500 px-2 py-2 bg-white rounded text-yellow-500 text-xl mx-4 lg:w-32 w-20 hover:bg-yellow-100">
          Current
        </button>
      </div>
      {!isLoading &&
        events.map((event: EventModel) => <EventCard event={event} />)}
    </div>
  );
};

export default Sidebar;
