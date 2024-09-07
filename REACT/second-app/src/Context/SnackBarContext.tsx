import { ReactNode, createContext, useState } from "react";
import Snackbar from "../Components/snackbar";

interface SnackData {
    showSomeMessage: (message: string) => void;
}


export const SnackContext = createContext<SnackData | undefined>(undefined);

interface SnackProviderProps {
    children: ReactNode;
}

export const SnackProvider: React.FC<SnackProviderProps> = ({ children }) => {
    const [active, setActive] = useState(false);
    const [message, setMessage] = useState('');

    const showSomeMessage = (msg: string) => {
        setMessage(msg);
        setActive(true);
        setTimeout(() => setActive(false), 3000);
    };

    const contextValue: SnackData = { showSomeMessage };

    return (
        <SnackContext.Provider value={contextValue}>
            {children}
            {active && <Snackbar message={message} />}
        </SnackContext.Provider>
    );
};
