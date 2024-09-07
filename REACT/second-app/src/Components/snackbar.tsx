const Snackbar = ({ message }: any) => {

    return (
        <div
            style={{
                position: 'fixed',
                bottom: '20px',
                right: '20px',
                backgroundColor: "yellowgreen",
                color: 'white',
                padding: '10px',
                borderRadius: '5px',
            }}
        >
            {message}
        </div>
    );
};

export default Snackbar