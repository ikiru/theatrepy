// Modules
import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";
import { NgbModule } from "@ng-bootstrap/ng-bootstrap";
import { FormsModule } from "@angular/forms";
import { HttpModule } from "@angular/http";
import { AppRoutingModule } from "./app-routing.module";
import { OAuthModule } from "angular-oauth2-oidc";

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
import { SpecialskillsService } from "./service/specialskills.service";
import { VocaltypeService } from "./service/vocaltype.service";
import { ShowlistService } from "./service/showlist.service";
import { RolelistService } from "./service/rolelist.service";
import { TechrolelistService } from "./service/techrolelist.service";
import { ConflictService } from "./service/conflict.service";
import { ConflictreasonService } from "./service/conflictreason.service";
import { AuditionService } from "./service/audition.service";
import { PublisherService } from "./service/publisher.service";
import { VenueService } from "./service/venue.service";
import { DirectorsnoteService } from "./service/directorsnote.service";
import { DonorService } from "./service/donor.service";
import { DonortypeService } from "./service/donortype.service";
import { BudgetcatagoryService } from "./service/budgetcatagory.service";

// Components
import { AppComponent } from "./app.component";
import { AboutComponent } from "./components/frontend/about/about.component";
import { MenuComponent } from "./components/frontend/menu/menu.component";
import { HeaderComponent } from "./components/frontend/header/header.component";
import { FooterComponent } from "./components/frontend/footer/footer.component";
import { NewsComponent } from "./components/frontend/news/news.component";
import { HomeComponent } from "./components/frontend/home/home.component";

@NgModule({
  declarations: [
    AppComponent,
    AboutComponent,
    MenuComponent,
    HeaderComponent,
    FooterComponent,
    NewsComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,
    NgModule,
    NgbModule,
    FormsModule,
    HttpModule,
    AppRoutingModule,
    OAuthModule.forRoot()
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
    DancetypeService,
    SpecialskillsService,
    VocaltypeService,
    ShowlistService,
    RolelistService,
    TechrolelistService,
    ConflictService,
    AuditionService,
    PublisherService,
    VenueService,
    DirectorsnoteService,
    DonorService,
    BudgetcatagoryService
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}
