import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class SchoolService {
  constructor(private _http: Http) {}

  createSchools(school) {
    return this._http
      .post("/school", school)
      .map(data => data.json())
      .toPromise();
  }
  getSchool(school) {
    return this._http
      .get("/school", school)
      .map(data => data.json())
      .toPromise();
  }
}
