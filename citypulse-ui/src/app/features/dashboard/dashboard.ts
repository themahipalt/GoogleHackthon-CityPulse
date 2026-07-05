import { Component, OnInit, inject } from '@angular/core';

import { CommonModule } from '@angular/common';

import { MatCardModule } from '@angular/material/card';

import { DashboardService } from '../../core/services/dashboard.service';

import { Dashboard } from '../../core/models/dashboard.model';


@Component({

    selector: 'app-dashboard',

    standalone: true,

    imports: [

        CommonModule,

        MatCardModule

    ],

    templateUrl: './dashboard.html',

    styleUrl: './dashboard.css'

})

export class DashboardComponent implements OnInit {

    private dashboardService = inject(DashboardService);

    dashboard?: Dashboard;

    ngOnInit(): void {

    console.log("Dashboard Loaded");

    this.dashboardService.getDashboard().subscribe({

        next: (response) => {

            console.log("API Response:", response);

            this.dashboard = response;

        },

        error: (error) => {

            console.error("API Error:", error);

        }

    });

}

}