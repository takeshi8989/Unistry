import { SchoolModel } from "../models.ts/School";
import { Link } from "react-router-dom";

const defaultImg: string =
  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOPRtwEAg8NC4x2Sg_E2DFKl9nn3Ku_J7_2g&usqp=CAU";
const SchoolCard: React.FC<{ school: SchoolModel }> = ({ school }) => {
  return (
    <div className="py-2 lg:w-2/5 w-4/5 border mt-2 flex">
      <div className="w-1/4 flex justify-center items-center">
        <img src={defaultImg} alt={school.name} className="w-full" />
      </div>
      <div className="w-3/4 flex flex-col justify-center">
        <Link to={"/school/" + school.id}>
          <p className="text-center text-2xl font-bold">{school.name}</p>
        </Link>
        <p className="text-right mr-2 mt-2">
          <span>{school.num_of_members} members </span>
          <span>{school.num_of_events} events</span>
        </p>
      </div>
    </div>
  );
};

export default SchoolCard;
