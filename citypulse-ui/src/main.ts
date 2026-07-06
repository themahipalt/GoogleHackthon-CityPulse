import { bootstrapApplication } from '@angular/platform-browser';

import { App } from './app/app';

import { appConfig } from './app/app.config';

import { Chart, registerables } from 'chart.js';

// Registers ALL chart types (line, pie, bar, radar, etc.)
Chart.register(...registerables);

bootstrapApplication(App, appConfig)
  .catch(err => console.error(err));