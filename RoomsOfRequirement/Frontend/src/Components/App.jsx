/* eslint-disable react/prefer-stateless-function */
import React, { Component } from 'react';
import { Provider } from 'react-redux';
import { HashRouter as Router, Switch, Route } from 'react-router-dom';

import Dashboard from './layout/Dashboard';
import store from '../store';
import ClassDetails from './layout/ClassDetails';

export default class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <Router>
          <Switch>
            <Route exact path="/" component={Dashboard} />
            <Route exact path="/:id" component={ClassDetails} />
          </Switch>
        </Router>
      </Provider>
    );
  }
}
