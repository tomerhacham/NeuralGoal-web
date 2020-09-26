import React, { Component } from "react";
import { Router, Switch, Route } from "react-router-dom";

import Table from '../components/Table'
import history from '../history';

export default class Routes extends Component {
    render() {
        return (
            <Router history={history}>
                <Switch>
                    <Route path="/" exact component={Table} />
                    <Route path="/Stats" component={Table} />
                    <Route path="/Foundation" component={Table} />
                    <Route path="/WinnerForm" component={Table} />
                </Switch>
            </Router>
        )
    }
}
