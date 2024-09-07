import Child from "./components/child";

function App() {
  const runSomething = () => {
    alert("i am pressed");
  };
  return (
    <>
      <Child buttonName="first-one" action={runSomething} />
    </>
  );
}

export default App;
