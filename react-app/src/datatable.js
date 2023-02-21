import * as React from 'react';
import Paper from '@mui/material/Paper';
import {DataGrid} from '@mui/x-data-grid';


function calculateScore(params) {
    return params.row.population ? ((params.row.gold_medals * 3
            + params.row.silver_medals * 2
            + params.row.bronze_medals) / (params.row.population / 1000000)
    ).toFixed(2) : 0
}

const columns = [
    {field: 'country', headerName: 'Country', sortable: false, width: 150},
    {field: 'gold_medals', headerName: 'Gold medals', type: 'number', width: 130},
    {field: 'silver_medals', headerName: 'Silver medals', type: 'number', width: 130},
    {field: 'bronze_medals', headerName: 'Bronze medals', type: 'number', width: 130},
    {field: 'population', headerName: 'Population', type: 'number', width: 150},
    {
        field: 'score',
        headerName: 'Score',
        type: 'number',
        width: 100,
        valueGetter: calculateScore,
    },
];

export default function DataTable(props) {
    return (
        <Paper>
            <div style={{height: 600, width: '100%'}}>
                <DataGrid
                    rows={props.medals}
                    columns={columns}
                    pageSize={10}
                    rowsPerPageOptions={[10]}
                    getRowId={(row) => row.country}
                />
            </div>
        </Paper>
    );
}

