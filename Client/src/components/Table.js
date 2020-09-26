import React, { useState } from "react";
import MUIDataTable from "mui-datatables";

function createData(
  league,
  date,
  homeTeam,
  awayTeam,
  homeOdds,
  drawOdds,
  awayOdds,
  pred1,
  predX,
  pred2
) {
  return [
    league,
    date,
    homeTeam,
    awayTeam,
    homeOdds,
    drawOdds,
    awayOdds,
    pred1,
    predX,
    pred2,
  ];
}

const rows = [
  createData(
    "Serie",
    "26/09/2020",
    "Lazio",
    "Cagliari",
    42.3,
    31.95,
    111.45,
    2.35,
    3.31,
    4.66
  ),
  createData(
    "Serie",
    "26/09/2020",
    "Torino",
    "Atlanta",
    4.3,
    3.95,
    1.45,
    0.35,
    0.31,
    0.66
  ),
  createData(
    "Serie",
    "26/09/2020",
    "Torino",
    "Atlanta",
    4.3,
    3.95,
    1.45,
    0.35,
    0.31,
    0.66
  ),
];

export default function EnhancedTable() {
  const [tableBodyHeight] = useState("100%");
  const [tableBodyMaxHeight] = useState("");

  const columns = [
    "League",
    "Date",
    "Home Team",
    "Away Team",
    "Home Odds",
    "Draw Odds",
    "Away Odds",
    "Prediction 1",
    "Prediction X",
    "Prediction 2",
  ];

  const options = {
    filter: true,
    print: false,
    filterType: "checkbox",
    tableBodyHeight,
    tableBodyMaxHeight,
    rowsPerPage: 100,
  };

  return (
    <MUIDataTable
      title={"Upcoming Games"}
      data={rows}
      columns={columns}
      options={options}
    />
  );
}
