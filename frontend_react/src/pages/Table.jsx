import { Box, useTheme } from "@mui/material";
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
        headerName: "Produccion (unidad: Kw)",
        type: "number",
        headerAlign: "left",
        align: "center",
        flex: 1,
    },
    {
        field: "Consumo general",
        headerName: "Consumo general (unidad: Kw)",
        type: "number",
        headerAlign: "left",
        align: "center",
        
        flex: 1,
    },
    {
        field: "Consumo controlado",
        headerName: "Consumo controlado (unidad: Kw)",
        type: "number",
        headerAlign: "left",
        align: "center",
        
        flex: 1,
    },
    {
        field: "Consumo Total",
        headerName: "Consumo Total (unidad: Kw)",
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
            <Header title="Table" subtitle="Managing the Table Members" />
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