import { Injectable, inject } from '@angular/core';

import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';

import { Dashboard } from '../models/dashboard.model';


@Injectable({
    providedIn: 'root'
})
export class DashboardService {

    private http = inject(HttpClient);

    private api = "http://localhost:8000";

    getDashboard(): Observable<Dashboard> {

        return this.http.get<Dashboard>(
            `${this.api}/dashboard`
        );

    }

}