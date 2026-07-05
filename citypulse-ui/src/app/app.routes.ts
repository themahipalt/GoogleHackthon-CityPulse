import { Routes } from '@angular/router';

import { DashboardComponent } from './features/dashboard/dashboard';
import { AnalyticsComponent } from './features/analytics/analytics';
import { ForecastComponent } from './features/forecast/forecast';
import { RecommendationsComponent } from './features/recommendations/recommendations';
import { ChatComponent } from './features/chat/chat';

export const routes: Routes = [
  {
    path: '',
    component: DashboardComponent
  },
  {
    path: 'analytics',
    component: AnalyticsComponent
  },
  {
    path: 'forecast',
    component: ForecastComponent
  },
  {
    path: 'recommendations',
    component: RecommendationsComponent
  },
  {
    path: 'chat',
    component: ChatComponent
  }
];