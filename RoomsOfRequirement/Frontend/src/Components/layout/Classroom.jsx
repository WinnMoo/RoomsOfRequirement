import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import { CardActionArea } from '@material-ui/core';

import '../App.css';

// eslint-disable-next-line react/prefer-stateless-function
export default class Classroom extends Component {
  static propTypes = {
    room: PropTypes.shape({
      classroom: PropTypes.string,
      times: PropTypes.arrayOf(
        PropTypes.shape({
          start_time: PropTypes.string,
          end_time: PropTypes.string,
        }),
      ),
    }).isRequired,
  };

  render() {
    const { room } = this.props;
    const { classroom, times } = room;
    return (
      <Link to={`/${classroom}`} style={{ textDecoration: 'none' }}>
        <Card className="Classroom-box" style={{ backgroundColor: '#ffa800' }}>
          <CardActionArea>
            <CardContent>
              <Typography component="h5" variant="h5" style={{ color: '#484236' }}>{classroom}</Typography>
              <Typography variant="subtitle1" color="textSecondary">
                {times.map(t => `${t.start_time}-${t.end_time}`).join(', ')}
              </Typography>
            </CardContent>
          </CardActionArea>
        </Card>
      </Link>
    );
  }
}
