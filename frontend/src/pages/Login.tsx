import { FcGoogle } from "react-icons/fc";
import { GrApple, GrGithub } from "react-icons/gr";

const Login: React.FC = () => {
  return (
    <div className="w-full pt-16 z-10 mb-20 h-full flex justify-center items-center">
      <div className="w-full sm:w-4/5 md:w-2/3 lg:w-1/2 mx-auto mt-16 flex flex-col">
        <form action="" className="flex flex-col items-center border-b-2">
          <h1 className="mt-4 text-2xl">Log in</h1>
          <p className="mt-2 text-md">
            Need to create an account?
            <a href="/signup" className="text-blue-500 ml-2">
              Sign up
            </a>
          </p>
          <div className="flex flex-col mt-3 w-1/2 mx-auto">
            <label htmlFor="email" className="text-xl">
              Email
            </label>
            <input
              className="border w-full h-10 border-2 rounded focus:outline-orange-200"
              id="email"
              type="email"
            />
          </div>
          <div className="flex flex-col mt-3 w-1/2 mx-auto">
            <label htmlFor="password" className="text-xl">
              Password:
            </label>
            <input
              className="border border-2 rounded focus:outline-orange-200 w-full h-10"
              id="password"
              type="password"
            />
          </div>

          <button className="my-3 border rounded py-3 px-6 text-xl bg-orange-300 text-white hover:bg-orange-400">
            Log in
          </button>
        </form>
        <div className="w-2/3 mx-auto mt-6">
          <div className="w-3/4 mx-auto h-16 flex items-center py-2 px-3 border border-2 rounded my-2">
            <FcGoogle size={30} className="w-1/4 w-full " />
            <p className="w-3/4 text-center text-xl">Log in with Google</p>
          </div>
          <div className="w-3/4 mx-auto h-16 flex items-center py-2 px-3 border border-2 rounded my-2">
            <GrApple size={30} className="w-1/4 w-full " />
            <p className="w-3/4 text-center text-xl">Log in with Apple</p>
          </div>
          <div className="w-3/4 mx-auto h-16 flex items-center py-2 px-3 border border-2 rounded my-2">
            <GrGithub size={30} className="w-1/4 w-full " />
            <p className="w-3/4 text-center text-xl">Log in with GitHub</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
