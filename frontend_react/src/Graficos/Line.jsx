
import { ResponsiveLine } from "@nivo/line";
import { useTheme } from "@mui/material";
import { tokens } from "../theme";

const LineChart = ({ data, isDashboard = false, rotate = false }) => {
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
          strokeWidth: 1.5,
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
        color: colors.grey[600],
      },
    },
  }

  return (
    <ResponsiveLine
      data={data}
      theme={chartTheme}
      colors={isDashboard ? { datum: "color" } : { scheme: "nivo" }} // nivo | paired | category10
      margin={{ top: 8, right: 100, bottom: 48, left: 60 }}
      xScale={{ type: "point" }}
      yScale={{
        type: "linear",
        min: "auto",
        max: "auto",
        stacked: false,
      }}
      yFormat=" >-.2f"
      curve="monotoneX"
      // curve='linear'
      lineWidth={3}

      axisTop={null}
      axisRight={null}
      axisBottom={{
        orient: "bottom",
        tickSize: 5,
        tickPadding: 10,
        tickRotation: rotate ? -45 : 0,
        legendOffset: 36,
        legendPosition: "middle",
      }}
      axisLeft={{
        orient: "left",
        tickValues: 5, // added
        tickSize: 5,
        tickPadding: 7,
        tickRotation: 0,
        legendOffset: -40,
        legendPosition: "middle",
      }}

      // enableSlices='x'
      enableGridX={false}
      enableGridY={false}
      enableCrosshair={true}

      enablePoints={false}

      // pointSize={8}
      // pointColor={{ theme: "background" }}
      // pointBorderWidth={2}
      // pointBorderColor={{ from: "serieColor" }}
      // pointLabelYOffset={-12}
      useMesh={true}

      legends={[
        {
          anchor: "bottom-right",
          direction: "column",
          justify: false,
          translateX: 100,
          translateY: 0,
          itemsSpacing: 0,
          itemDirection: "left-to-right",
          itemWidth: 80,
          itemHeight: 20,
          itemOpacity: 0.75,
          symbolSize: 12,
          symbolShape: "circle",
          symbolBorderColor: "rgba(0, 0, 0, .5)",
          effects: [
            {
              on: "hover",
              style: {
                itemBackground: "rgba(0, 0, 0, .03)",
                itemOpacity: 1,
              },
            },
          ],
        },
      ]}
    />
  );
};

export default LineChart;