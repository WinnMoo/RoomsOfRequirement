/* eslint-disable camelcase */
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import { CardActionArea } from '@material-ui/core';

// eslint-disable-next-line react/prefer-stateless-function
export default class Classroom extends Component {
  static propTypes = {
    room: PropTypes.shape({
      classroom: PropTypes.string,
      start_time: PropTypes.string,
      end_time: PropTypes.string,
    }).isRequired,
  };

  render() {
    const { room } = this.props;
    const { classroom, start_time, end_time } = room;
    return (
      <Card className="Classroom-box">
        <CardActionArea>
          <CardContent>
            <Typography component="h5" variant="h5">{classroom}</Typography>
            <Typography variant="subtitle1" color="textSecondary">{`${start_time}-${end_time}`}</Typography>
          </CardContent>
        </CardActionArea>
      </Card>
    );
  }
}
