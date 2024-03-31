import { Routes } from '@angular/router';

import { DashboardComponent } from './dashboard/dashboard.component';
import { QuestionsComponent } from './questions/questions.component';

export const routes: Routes = [
    // define paths for dashboard students and subjects
    {
        path: '',
        component: DashboardComponent
    },
    {
        path: 'questions',
        component: QuestionsComponent
    }
];