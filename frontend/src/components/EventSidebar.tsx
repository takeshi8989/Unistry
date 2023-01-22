import { EventModel } from "../models.ts/Event";

const EventSidebar = ({ event }: { event: EventModel }) => {
  return (
    <div className="border-x md:h-screen w-full mt-1 flex flex-col items-center">
      <p className="text-center mt-4 mb-2 font-bold" style={{ fontSize: 30 }}>
        Organizers
      </p>
      {event.organizers.map((organizer) => (
        <div className="lg:flex mt-2" key={organizer}>
          <img
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOPRtwEAg8NC4x2Sg_E2DFKl9nn3Ku_J7_2g&usqp=CAU"
            alt="organizer"
            className="w-16 lg:mx-2 mx-auto"
          />
          <p className="text-center text-2xl mt-4 mb-4">Takeshi Hashimoto</p>
        </div>
      ))}

      <div className="flex justify-center mb-4"></div>
      <p className="text-center mt-4 mb-2 font-bold" style={{ fontSize: 30 }}>
        Members
      </p>
      <div className="flex flex-wrap justify-center">
        {event.members.map((profile) => (
          <div className="flex flex-col" key={profile}>
            <img
              src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOPRtwEAg8NC4x2Sg_E2DFKl9nn3Ku_J7_2g&usqp=CAU"
              alt="organizer"
              className="w-16 mx-2"
            />
            <p className="text-center mb-2">{profile}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default EventSidebar;
