import { Box } from "@mui/material";
import Header from "../components/Header";


const Dashboard = () => {

    return (
        <Box m='1.25rem'>
            <Box display='flex' justifyContent='space-between' alignItems='center'>
                <Header title='DASHBOARD' subtitle='Bienvenido a tu dashboard'/>
            </Box>
            Dashboard
        </Box>
    )
}

export default Dashboard;