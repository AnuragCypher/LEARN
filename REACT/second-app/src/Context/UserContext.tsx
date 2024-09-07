import React, { createContext } from "react"

interface UserDataType {
    name: string
    age: number
}

interface UserProvider {
    value: UserDataType
    children: React.ReactNode
}

export const UserContext = createContext<UserDataType | undefined>(undefined);

export const UserProvider: React.FC<UserProvider> = ({ value, children }) => {
    return <UserContext.Provider value={value}>{children}</UserContext.Provider>
}
