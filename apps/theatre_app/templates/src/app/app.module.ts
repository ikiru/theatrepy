// Modules
import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";
import { NgbModule } from "@ng-bootstrap/ng-bootstrap";
import { FormsModule } from "@angular/forms";
import { HttpModule } from "@angular/http";
import { AppRoutingModule } from "./app-routing.module";

// Components
import { AppComponent } from "./app.component";

// Services
import { StateService } from "./service/state.service";
import { SchoolService } from "./service/school.service";
import { DistrictService } from "./service/district.service";

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    NgModule,
    NgbModule,
    FormsModule,
    HttpModule,
    AppRoutingModule
  ],
  providers: [StateService, SchoolService, DistrictService],
  bootstrap: [AppComponent]
})
export class AppModule {}
