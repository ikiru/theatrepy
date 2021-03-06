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
    return this._http.get("/school").map(data => data.json()).toPromise();
  }
  updateSchool(school) {
    return this._http
      .patch(`/school/${school._id}`, school)
      .map(data => data.json())
      .toPromise();
  }

  destroySchool(id: string) {
    return this._http
      .delete(`/school/${id}`)
      .map(data => data.json())
      .toPromise();
  }
}
