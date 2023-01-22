import EventSidebar from "../components/EventSidebar";
import useWindowSize from "../hooks/useWIndowSize";
import { EventModel } from "../models.ts/Event";
import useFetch from "../hooks/useFetch";
import { useParams } from "react-router-dom";
import TeamCard from "../components/TeamCard";

const Event = () => {
  const windowSize = useWindowSize();
  const params = useParams();
  const [event, isLoading, error, refetch]: [
    EventModel,
    boolean,
    any,
    () => void
  ] = useFetch(`/events/${params.id}/`);

  if (error) {
    console.log(error);
    refetch();
  }

  return (
    <div className="h-full w-full md:flex pt-20 relative z-10">
      {windowSize >= 768 && !isLoading && (
        <div className="w-1/3 h-full">
          <EventSidebar event={event} />
        </div>
      )}
      {!isLoading && (
        <div className="md:w-2/3 w-full mt-10">
          <h1
            className="text-center"
            style={{
              fontSize:
                windowSize >= 768 ? Math.floor((windowSize * 70) / 1600) : 40,
            }}
          >
            {event.title}
          </h1>
          <p className="text-right mr-16 mt-4 text-2xl">
            School: {event.school}
          </p>
          <p className="text-right mr-12 mt-4 text-lg">{event.created_at} ~</p>

          <div className="lg:w-1/2 w-5/6 mx-auto mt-10">
            <p className="text-center text-2xl">Event Info</p>
            <p className="text-lg mt-5 text-center">{event.description}</p>
          </div>
          <div className="lg:w-3/4 w-full mx-auto mt-10">
            <p className="text-center text-2xl">Teams</p>
            <div className="flex flex-wrap justify-between">
              {event.teams.map((team) => (
                <TeamCard team={team} />
              ))}
            </div>
          </div>
        </div>
      )}

      {windowSize < 768 && !isLoading && (
        <div className="">
          <EventSidebar event={event} />
        </div>
      )}
    </div>
  );
};

export default Event;
