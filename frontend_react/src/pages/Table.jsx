import { Box, colors, useTheme } from "@mui/material";
import { DataGrid } from '@mui/x-data-grid';

import { tokens } from '../theme';
import { useEffect, useState } from "react";

import Header from "../components/Header";
import axiosI from "../api";

const columns = [
    { field: "id", headerName: "ID" },
    {
        field: "Fecha",
        //   headerName: "Name",
        type: 'date',
        //   width: '5rem',
        cellClassName: "name-column--cell",
    },
    {
        field: "Produccion",
        headerName: "Produccion (Kw)",
        type: "number",
        headerAlign: "left",
        align: "center",
        flex: 1,
    },
    {
        field: "Consumo general",
        headerName: "Consumo general (Kw)",
        type: "number",
        headerAlign: "left",
        align: "center",
        
        flex: 1,
    },
    {
        field: "Consumo controlado",
        headerName: "Consumo controlado (Kw)",
        type: "number",
        headerAlign: "left",
        align: "center",
        
        flex: 1,
    },
    {
        field: "Diferencia",
        headerName: "Diferencia (Kw)",
        type: "number",
        headerAlign: "left",
        align: "center",
        flex: 1,
        renderCell: (d) => {
            const value = d.formattedValue;
            const positive = value >= 0;
            console.log(d);
            
            return (
            <Box 
                color={positive ? '#9CFF2E': '#F00'}
                fontWeight='bold'
            >
                {positive && '+'} {value} Kw
            </Box>
        )}
    },
    {
        field: "Consumo Total",
        headerName: "Consumo Total (Kw)",
        type: "number",
        headerAlign: "left",
        align: "center",
        
        flex: 1,
    },
];

const Table = () => {

    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const [tableData, setTableData] = useState([]);

    useEffect(() => {
        const requestData = async () => {
            const response = await axiosI('table')
            console.log(response.data)

            setTableData(response.data);
        }

        requestData();
    }, [])

    return (
        <Box>
            <Header title="Tabla de datos" subtitle="Resumen diario de los datos del sistema." />
            <Box
                m="40px 0 0 0"
                height="75vh"
                sx={{
                    "& .MuiDataGrid-root": {
                        border: "none",
                    },
                    "& .MuiDataGrid-cell": {
                        borderBottom: "none",
                        backgroundColor: colors.grey[500]
                    },
                    "& .name-column--cell": {
                        color: colors.secondary[300]
                    },
                    "& .MuiDataGrid-columnHeaders": {
                        backgroundColor: colors.blueAccent[700],
                        borderBottom: "none",
                    },
                    "& .MuiDataGrid-virtualScroller": {
                        backgroundColor: colors.grey[900]
                    },
                    "& .MuiDataGrid-footerContainer": {
                        borderTop: "none",
                        backgroundColor: colors.blueAccent[700],
                    },
                    "& .MuiCheckbox-root": {
                        color: `${colors.secondary[200]} !important`,
                    },
                }}
            >
                <DataGrid 
                    checkboxSelection 
                    rows={tableData} 
                    columns={columns} 
                />
            </Box>
        </Box>
    )
}

export default Table;