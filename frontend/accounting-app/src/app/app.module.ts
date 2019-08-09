import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms'
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppDashboardComponent } from './app-dashboard/app-dashboard.component';
import { AppRoutingModule } from './app-routing.module';
import { LoginComponent } from './login/login.component';

import { MatToolbarModule,
         MatCardModule, 
         MatFormFieldModule, 
         MatProgressSpinnerModule, 
         MatInputModule,
         MatButtonModule, 
         MatDialogModule,
         MatTableModule, 
         MatMenuModule, 
         MatIconModule, 
         MatListModule, 
         MatGridListModule } from '@angular/material';



@NgModule({
  declarations: [
    AppComponent,
    AppDashboardComponent,
    LoginComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    MatToolbarModule,
    MatCardModule,
    MatFormFieldModule,
    MatProgressSpinnerModule,
    MatInputModule,
    MatButtonModule, 
    MatDialogModule,
    MatTableModule,
    MatMenuModule,
    MatIconModule,
    MatListModule,
    MatGridListModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
