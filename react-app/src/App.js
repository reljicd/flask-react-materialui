import * as React from 'react';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import ButtonGroup from '@mui/material/ButtonGroup';
import {Box, Stack} from "@mui/material";
import DataTable from "./datatable";


const backend_api = 'http://localhost:5002/medals'
export default class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            medals: [],
            years: ['All time'],
            currentYear: 'All time'
        };
        this.buttonClicked = this.buttonClicked.bind(this);
    }

    componentDidMount() {
        fetch(backend_api + '/years')
            .then(response => response.json())
            .then(years => this.setState({
                years: this.state.years.concat(years)
            }));

        fetch(backend_api + '/per_country')
            .then(response => response.json())
            .then(medals => this.setState({
                medals: medals
            }));

    }

    buttonClicked(year) {
        let api_url = backend_api + '/per_country/' + year
        if (year === 'All time') {
            api_url = backend_api + '/per_country'
        }

        fetch(api_url)
            .then(response => response.json())
            .then(medals => this.setState({
                medals: medals,
                currentYear: year
            }));

    }

    render() {
        const buttons = this.state.years.map((year) =>
            <Button key={year}
                    onClick={() => this.buttonClicked(year)}>
                {year}
            </Button>);

        return (
            <Container maxWidth="md">
                <Stack direction='row' justifyContent='center'>
                    <Typography variant="h3" allign="center" gutterBottom>
                        Olympic Medals Winners
                    </Typography>
                </Stack>

                <Box component="span" sx={{p: 2}}>
                    <Stack direction='row' justifyContent='center'>
                        <ButtonGroup variant="contained" aria-label="outlined primary button group">
                            {buttons}
                        </ButtonGroup>
                    </Stack>
                </Box>

                <Stack direction='row' justifyContent='center'>
                    <Typography variant="h6" allign="center" gutterBottom>
                        {this.state.currentYear}
                    </Typography>
                </Stack>

                < DataTable medals={this.state.medals}/>

                <Typography variant="body2">
                    * Score = (gold medals * 3 + silver medals * 2 + bronze medals) / population in millions
                </Typography>
            </Container>
        );
    }
}
