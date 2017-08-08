// Modules
import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";
import { NgbModule } from "@ng-bootstrap/ng-bootstrap";
import { FormsModule } from "@angular/forms";
import { HttpModule } from "@angular/http";
import { AppRoutingModule } from "./app-routing.module";

// Services
import { StateService } from "./service/state.service";
import { SchoolService } from "./service/school.service";
import { DistrictService } from "./service/district.service";
import { GradyearService } from "./service/gradyear.service";
import { TcatagoryService } from "./service/tcatagory.service";
import { ThonorService } from "./service/thonor.service";
import { TlengthService } from "./service/tlength.service";
import { TpositionService } from "./service/tposition.service";
import { TrankService } from "./service/trank.service";
import { DancetypeService } from "./service/dancetype.service";

// Components
import { AppComponent } from "./app.component";

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
  providers: [
    StateService,
    SchoolService,
    DistrictService,
    GradyearService,
    TcatagoryService,
    ThonorService,
    TlengthService,
    TpositionService,
    TrankService,
    DancetypeService
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}
