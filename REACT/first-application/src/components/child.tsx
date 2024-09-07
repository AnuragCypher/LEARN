import React from "react";

const Child: React.FC<{ buttonName: string; action: () => void }> = ({
  buttonName,
  action,
}) => {
  return (
    <>
      <button onClick={() => action()}>{buttonName}</button>
    </>
  );
};

export default Child;
