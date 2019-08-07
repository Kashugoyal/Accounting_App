import { AppDashboardComponent } from './app-dashboard/app-dashboard.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';


const routes: Routes = [
  { path: '', component: AppDashboardComponent }
];

@NgModule({
  declarations: [],
  imports: [
  RouterModule.forRoot(routes)
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule { } 
