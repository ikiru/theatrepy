// Modules
import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";
// import { LoginComponent } from "./login/login.component";
// import { DashboardComponent } from "./dashboard/dashboard.component";

// Routes
const routes: Routes = [
  // { path: "", pathMatch: "full", component: LoginComponent },
  // { path: "dashboard", component: DashboardComponent }
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
