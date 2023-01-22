import { BiRightArrow } from "react-icons/bi";
import { MdPlayArrow } from "react-icons/md";
import { SlPaperPlane } from "react-icons/sl";
import Message from "../components/Message";
import useWindowSize from "../hooks/useWIndowSize";

const chats: number[] = [1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1];

const Chat = () => {
  const windowSize = useWindowSize();
  return (
    <div className="h-full w-full lg:flex md:pt-20 pt-16 z-10">
      {windowSize < 1024 && (
        <div className="w-full mx-auto border-b flex overflow-x-scroll fixed z-20 bg-white">
          {chats.map((chat, index) => (
            <div className="w-20 m-4">
              <img
                src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOPRtwEAg8NC4x2Sg_E2DFKl9nn3Ku_J7_2g&usqp=CAU"
                alt="logo"
                className="w-full"
              />
              {index === 0 ? (
                <p className="font-bold text-center">name</p>
              ) : (
                <p className="text-center">name</p>
              )}
            </div>
          ))}
        </div>
      )}
      {windowSize >= 1024 && (
        <div className="w-1/3 h-full flex pt-10 items-center justify-start flex-col border-r overflow-y-scroll">
          {chats.map((chat, index) => (
            <div className="flex items-center my-3">
              {index === 2 ? (
                <MdPlayArrow size={30} className="mr-6 ml-4" />
              ) : (
                <BiRightArrow size={20} className="mr-2" />
              )}
              <img
                src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOPRtwEAg8NC4x2Sg_E2DFKl9nn3Ku_J7_2g&usqp=CAU"
                alt="logo"
                className="w-20 h-20"
              />
              <div>
                <p className="text-2xl mx-4">Event/Team1</p>
              </div>
            </div>
          ))}
        </div>
      )}

      <div className="lg:w-2/3 w-full pt-20">
        <div className="lg:h-5/6 h-1/2 overflow-y-scroll">
          <Message mine={false} />
          <Message mine={true} />
          <Message mine={false} />
          <Message mine={false} />
          <Message mine={true} />
          <Message mine={false} />
        </div>
        <div className="lg:w-2/3 w-full mt-4 fixed bottom-0 bg-white">
          <div className="relative md:w-2/3 w-full mx-auto">
            <textarea className="w-full mx-auto lg:h-20 h-14 bg-white pr-24 resize-none border border-2 rounded focus:outline-gray-200 lg:text-lg"></textarea>
            <button className="absolute px-3 lg:h-16 h-12 w-16 md:w-20 lg:top-2 top-1 rounded text-white bg-white border border-2 border-sky-600  right-2 flex justify-center items-center">
              <SlPaperPlane size={30} color="blue" className="mt-1" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Chat;
