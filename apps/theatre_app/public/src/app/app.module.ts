// Modules  and work
import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";
import { NgbModule } from "@ng-bootstrap/ng-bootstrap";
import { FormsModule } from "@angular/forms";
import { HttpModule } from "@angular/http";
// import { AppRoutingModule } from "./app-routing.module";

// Components
import { AppComponent } from "./app.component";

// Services
import { SchoolService } from "./school.service";

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    NgModule,
    NgbModule,
    FormsModule,
    HttpModule
    // AppRoutingModule
  ],
  providers: [SchoolService],
  bootstrap: [AppComponent]
})
export class AppModule {}
