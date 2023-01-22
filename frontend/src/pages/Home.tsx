import React from "react";
import SchoolCard from "../components/SchoolCard";
import SideEvents from "../components/SideEvents";
import useWindowSize from "../hooks/useWIndowSize";
import { SchoolModel } from "../models.ts/School";
import useFetch from "../hooks/useFetch";
// const url = "http://unistry-env.eba-nvfnbve2.us-west-2.elasticbeanstalk.com/"
const Home: React.FC = () => {
  const windowSize = useWindowSize();
  const [schools, isLoading, error, refetch] = useFetch(`/schools/`);

  if (error) {
    console.log(error);
    refetch();
  }

  return (
    <div className="h-screen w-full md:flex pt-20 relative z-10">
      {windowSize >= 768 && (
        <div className="w-1/3 h-full">
          <SideEvents title={"Popular Events"} />
        </div>
      )}
      {!isLoading && (
        <div className="md:w-2/3 w-full">
          <h1 className="text-center text-2xl mt-5">Active Schools</h1>
          <div className="flex flex-wrap lg:justify-between justify-center mx-auto w-4/5 mt-4">
            {schools.map((school: SchoolModel) => (
              <SchoolCard key={school.id} school={school} />
            ))}
          </div>
        </div>
      )}
      {windowSize < 768 && (
        <div className="w-full">
          <SideEvents title={"Popular Events"} />
        </div>
      )}
    </div>
  );
};

export default Home;
