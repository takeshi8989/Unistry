import React from "react";
import { EventModel } from "../models.ts/Event";
import { Link } from "react-router-dom";

const EventCard: React.FC<{ event: EventModel }> = ({ event }) => {
  return (
    <>
      <div className="w-2/3 mx-auto my-2 border">
        <Link to={"/event/" + event.id}>
          <p className="text-center text-2xl font-bold">{event.title}</p>

          <p className="text-center text-xl">School: {event.school}</p>
          <p className="text-center text-lg ">{event.created_at} ~</p>
          <p className="text-center">{event.description}</p>
          <p className="text-right mr-2">
            {event.members.length} members attended
          </p>
        </Link>
      </div>
    </>
  );
};

export default EventCard;
