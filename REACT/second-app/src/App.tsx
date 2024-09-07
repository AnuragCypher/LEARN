import First from "./Components/first"
import { SnackProvider } from "./Context/SnackBarContext"
import { UserProvider } from "./Context/UserContext"

function App() {

  return (
    <>
      <SnackProvider>
        <UserProvider value={{ name: "anurag", age: 23 }}>
          <First />
        </UserProvider>
      </SnackProvider>
    </>
  )
}

export default App
