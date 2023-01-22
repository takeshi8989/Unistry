import React from "react";
import { EventTeam } from "../models.ts/Event";

const TeamCard: React.FC<{ team: EventTeam }> = ({ team }) => {
  return (
    <div className="sm:w-2/5 w-full border m-6 p-3">
      <p className="text-center text-2xl font-bold">Team 1</p>
      <p className="text-center mb-1">Members</p>
      <div className="flex flex-wrap justify-center">
        {team.members.map((t) => (
          <img
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOPRtwEAg8NC4x2Sg_E2DFKl9nn3Ku_J7_2g&usqp=CAU"
            alt="profile"
            className="w-1/5 mx-1"
          />
        ))}
      </div>
    </div>
  );
};

export default TeamCard;
