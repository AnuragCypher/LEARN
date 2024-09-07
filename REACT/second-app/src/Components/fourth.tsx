import { useContext } from "react"
import { UserContext } from "../Context/UserContext"
import { SnackContext } from "../Context/SnackBarContext"

const Fourth = () => {
    const user = useContext(UserContext)
    const snack = useContext(SnackContext)
    return (
        <>
            <div>
                <p>name : {user?.name}</p>
            </div>
            <div>
                <p>age: {user?.age}</p>
            </div >

            <button onClick={() => { snack?.showSomeMessage("HELLO") }}>SHOW MESSAGE</button>
        </>
    )
}

export default Fourth