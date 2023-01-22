import { BsSearch } from "react-icons/bs";
import useWindowSize from "../hooks/useWIndowSize";

const members: number[] = [
  1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1, 1, 1, 11, 1, 1, 11, 1, 1, 1, 1, 1, 1, 1, 1,
  1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1, 1, 1,
];

const Members = () => {
  const windowSize = useWindowSize();
  return (
    <div className="h-full w-full md:flex pt-20 relative z-10">
      <div className="md:w-1/3 w-full md:h-full border flex justify-center items-center">
        <img
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOPRtwEAg8NC4x2Sg_E2DFKl9nn3Ku_J7_2g&usqp=CAU"
          alt="logo"
          className="w-1/4 ml-4"
        />
        <h1
          className="text-center ml-2"
          style={{ fontSize: windowSize >= 1024 ? 40 : 30 }}
        >
          School Name
        </h1>
      </div>
      {windowSize < 768 && (
        <div className="relative flex justify-start mx-auto w-4/5 mx-auto md:w-2/3 mt-10 pb-5">
          <BsSearch className="absolute mt-3 ml-2" size={25} color="gray" />
          <input
            type="text"
            className="text-lg pl-10 border border-1 rounded md:w-1/2 w-full h-12 focus:outline-sky-200"
            placeholder="Search members"
          />
        </div>
      )}

      <div className="md:w-2/3 w-full right-0 h-full overflow-y-scroll">
        {windowSize >= 768 && (
          <div className="relative flex justify-start mx-auto w-2/3 mt-10">
            <BsSearch className="absolute mt-3 ml-2" size={25} color="gray" />
            <input
              type="text"
              className="text-lg pl-10 border border-1 rounded w-1/2 h-12 focus:outline-sky-200"
              placeholder="Search members"
            />
          </div>
        )}
        <div className="mb-60">
          {members.map((member) => (
            <div className="w-2/3 mx-auto flex mt-10 items-center">
              <img
                src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOPRtwEAg8NC4x2Sg_E2DFKl9nn3Ku_J7_2g&usqp=CAU"
                alt="logo"
                className="w-20"
              />
              <div>
                <p className="text-2xl mx-4 mt-2">Takeshi Hashimoto</p>
                <p className="ml-28">Joined Jul 25, 2021</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Members;
