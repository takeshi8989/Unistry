interface Props {
  mine: boolean;
}

const Message = ({ mine }: Props) => {
  if (mine) {
    return (
      <div className="flex mr-10 justify-end mt-4 mb-10">
        <div className="w-1/2">
          <p className="text-right text-2xl mr-2">Name</p>
          <p className="mr-2 md:text-lg text-md">
            Hi this is the message contentHi this is the message content Hi this
            is the message content Hi this is the message contentHi this is the
            message contentHi this is the message contentHi this is the message
            contentHi this is the message content
          </p>
          <p className="text-lg mr-3 mt-2 text-right"> 12:32</p>
        </div>
        <img
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOPRtwEAg8NC4x2Sg_E2DFKl9nn3Ku_J7_2g&usqp=CAU"
          alt="logo"
          className="md:w-20 md:h-20 w-10 h-10"
        />
      </div>
    );
  } else {
    return (
      <div className="flex ml-10 mt-4 mb-10">
        <img
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOPRtwEAg8NC4x2Sg_E2DFKl9nn3Ku_J7_2g&usqp=CAU"
          alt="logo"
          className="md:w-20 md:h-20 w-10 h-10"
        />
        <div className="w-1/2">
          <p className="text-2xl ml-2">Name</p>
          <p className="ml-2 md:text-lg text-md">
            Hi this is the message contentHi this is the message content Hi this
            is the message content Hi this is the message contentHi this is the
            message contentHi this is the message contentHi this is the message
            contentHi this is the message content
          </p>
          <p className="text-lg ml-3 mt-2"> 12:32</p>
        </div>
      </div>
    );
  }
};

export default Message;
