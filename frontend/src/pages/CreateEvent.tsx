import React from "react";

const organizers: number[] = [1, 1, 1, 1];

const CreateEvent: React.FC = () => {
  return (
    <div className="w-full pt-16 z-10 mb-20 ">
      <div className="sm:w-3/4 md:w-1/2 w-full mx-auto border border-2 border-black rounded mt-10">
        <form action="" className="flex flex-col items-center">
          <h1 className="text-2xl mt-4">Create a New Event</h1>
          <p className="text-2xl mt-4">School: Langara College</p>
          <div className="flex mt-3">
            <label htmlFor="event-name" className="text-xl">
              Event Name:
            </label>
            <input
              className="mx-2 border border-2 rounded focus:outline-orange-200"
              id="event-name"
              type="text"
            />
          </div>
          <div className="mt-3 flex lg:flex-row flex-col">
            <label className="text-xl text-center" htmlFor="organizers">
              Add up to other 3 organizers:
            </label>
            <input
              type="text"
              placeholder="type username or email"
              className="pl-1 mx-2 mt-2 lg:mt-0 border border-2 rounded focus:outline-orange-200"
            />
          </div>
          <div className="flex flex-wrap justify-center mt-2">
            {organizers.map((organizer) => (
              <div className="flex items-center lg:w-1/2 w-full justify-center mx-auto">
                <img
                  src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOPRtwEAg8NC4x2Sg_E2DFKl9nn3Ku_J7_2g&usqp=CAU"
                  alt="profile"
                  className="w-10 h-10 mr-1"
                />
                <p>Takeshi Hashimoto</p>
              </div>
            ))}
          </div>
          <div className="mt-2 w-2/3 mx-auto">
            <p className="text-xl text-center mb-2">Event Description</p>
            <textarea
              name=""
              id="description"
              className="w-full resize-none h-32 border border-2 rounded focus:outline-orange-200"
            ></textarea>
          </div>
          <div className="flex mt-3">
            <label className="text-xl" htmlFor="is-public">
              Public Event:
            </label>
            <select
              name=""
              id="is-public"
              className="mx-2 text-xl focus:outline-none"
            >
              <option value="Yes">Yes</option>
              <option value="No">No</option>
            </select>
          </div>
          <div className="text-lg flex mt-3 lg:flex-row flex-col">
            <p className="text-xl mx-3 mb-2 lg:mb-0">
              How many people do you want?
            </p>
            <div className="flex justify-center">
              <label htmlFor="min" className="text-xl">
                min
              </label>
              <input
                type="number"
                id="min"
                min="1"
                max="99"
                defaultValue="4"
                className="w-12 mx-2 text-center focus:outline-none"
              />
              <label htmlFor="max" className="text-xl">
                max
              </label>
              <input
                type="number"
                id="max"
                min="4"
                max="100"
                defaultValue="30"
                className="w-12 mx-2 text-center focus:outline-none"
              />
            </div>
          </div>
          <button className="my-3 border rounded py-3 px-6 text-xl bg-orange-300 text-white hover:bg-orange-400">
            Create
          </button>
        </form>
      </div>
    </div>
  );
};

export default CreateEvent;
