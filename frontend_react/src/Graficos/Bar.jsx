import { ResponsiveBar } from "@nivo/bar";
import { useTheme } from "@mui/material";
import { tokens } from "../theme";

const BarChart = ({ data, keys, indexBy, tickLeft = 5}) => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const chartTheme = {
        axis: {
          domain: {
            line: {
              stroke: colors.grey[100],
            },
          },
          legend: {
            text: {
              fill: colors.grey[100],
            },
          },
          ticks: {
            line: {
              stroke: colors.grey[100],
            },
            text: {
              fill: colors.grey[100],
            },
          },
        },
        legends: {
          text: {
            fill: colors.grey[100],
          },
        },
        tooltip: {
          container: {
            color: colors.primary[500],
          },
        },
      }

    return (
        <ResponsiveBar
            data={data && data.length > 1? data : []}
            theme={chartTheme}
            keys={keys}
            indexBy={indexBy}
            margin={{ top: 10, right: 10, bottom: 50, left: 30 }}
            padding={0.3}
            valueScale={{ type: 'linear' }}
            indexScale={{ type: 'band', round: true }}
            colors={{ scheme: 'category10' }} // nivo | paired | category10
            axisTop={null}
            axisRight={null}
            axisBottom={
                {
                tickSize: 2,
                tickPadding: 6,
                tickRotation: 0
            }
            }
            axisLeft={{
                tickValues: tickLeft,
                tickSize: 2,
                tickPadding: 6,
                tickRotation: 0,
            }}
            // labelSkipWidth={12}
            // labelSkipHeight={12}
            enableLabel={false}
            enableGridY={false}
        />
          
    )
}

export default BarChart;