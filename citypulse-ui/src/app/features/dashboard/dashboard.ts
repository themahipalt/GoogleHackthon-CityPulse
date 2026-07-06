import { Component, OnInit, inject } from '@angular/core';

import { CommonModule } from '@angular/common';

import { MatCardModule } from '@angular/material/card';

import { BaseChartDirective } from 'ng2-charts';

import {
    ChartConfiguration,
    ChartOptions
} from 'chart.js';

import { DashboardService } from '../../core/services/dashboard.service';

import { Dashboard } from '../../core/models/dashboard.model';

@Component({

    selector: 'app-dashboard',

    standalone: true,

    imports: [

        CommonModule,

        MatCardModule,

        BaseChartDirective

    ],

    templateUrl: './dashboard.html',

    styleUrl: './dashboard.css'

})

export class DashboardComponent implements OnInit {
  constructor() {
    console.log("Dashboard Component Loaded");
}

    private dashboardService = inject(DashboardService);

    dashboard?: Dashboard;

    lineChartData: ChartConfiguration<'line'>['data'] = {

        labels: [],

        datasets: [

            {

                label: 'Complaints',

                data: [],

                fill: false,

                tension: 0.3

            }

        ]

    };

    lineChartOptions: ChartOptions<'line'> = {

        responsive: true,

        maintainAspectRatio: false

    };

    ngOnInit(): void {

        console.log("Dashboard Loaded");

        this.loadDashboard();

        this.loadTrend();

    }

    loadDashboard(): void {

        console.log("Calling Dashboard API...");

        this.dashboardService.getDashboard().subscribe({

            next: (response: Dashboard) => {

                console.log("========== API ==========");
                console.log(response);

                this.dashboard = response;

                console.log("========== DASHBOARD ==========");
                console.log(this.dashboard);

            },

            error: (error) => {

                console.error("Dashboard API Error");
                console.error(error);

            }

        });

    }

    loadTrend(): void {

        console.log("Calling Trend API...");

        this.dashboardService.getTrend().subscribe({

            next: (response) => {

                console.log("========== TREND ==========");
                console.log(response);

                this.lineChartData = {

                    labels: response.map(x => x.day),

                    datasets: [

                        {

                            label: 'Complaints',

                            data: response.map(x => x.total),

                            fill: false,

                            tension: 0.3

                        }

                    ]

                };

                console.log("Chart Updated");

            },

            error: (error) => {

                console.error("Trend API Error");
                console.error(error);

            }

        });

    }

}