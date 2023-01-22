import SideEvents from "../components/SideEvents";
import useWindowSize from "../hooks/useWIndowSize";

const Profile = () => {
  const windowSize = useWindowSize();
  return (
    <div className="h-screen w-full flex pt-20 relative z-10">
      {windowSize >= 768 && (
        <div className="w-1/3 h-full">
          <SideEvents title={"Pinned Events"} />
        </div>
      )}
      <div className="md:w-2/3 w-full">
        <div className="flex justify-center mt-10 items-center mb-5">
          <img
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOPRtwEAg8NC4x2Sg_E2DFKl9nn3Ku_J7_2g&usqp=CAU"
            alt="profile"
            className="mr-6 w-1/5"
          />
          <h1
            className="text-center"
            style={{
              fontSize:
                windowSize >= 768 ? Math.floor((windowSize * 60) / 1600) : 30,
            }}
          >
            Takeshi Hashimoto
          </h1>
        </div>

        <div className="w-4/5 mx-auto mt-5">
          <p
            className="text-center mb-5"
            style={{ fontSize: windowSize >= 640 ? 30 : 20 }}
          >
            <a className="text-blue-600" href="https://github.com/takeshi8989">
              https://github.com/takeshi8989
            </a>
          </p>
          <p
            className="text-center"
            style={{ fontSize: windowSize >= 640 ? 40 : 30 }}
          >
            School: Langara College
          </p>
          <p
            className="text-center"
            style={{ fontSize: windowSize >= 640 ? 40 : 30 }}
          >
            Attended 100 Events
          </p>
          <p
            className="text-center"
            style={{ fontSize: windowSize >= 640 ? 40 : 30 }}
          >
            Organized 11 Events
          </p>
          <p className="text-center mt-10 mb-10 md:w-2/3 text-xl w-full mx-auto">
            Hi, I am studying Computer Science at Langara College. aldfjalkjf
            dl;sajflkdajslkjd flkasjfldkasjl;k dfjalk;sjfd;lksanflkdnsa
          </p>
        </div>
        {windowSize < 768 && (
          <div className="">
            <SideEvents title={"Pinned Events"} />
          </div>
        )}
      </div>
    </div>
  );
};

export default Profile;
