import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class RolelistService {
  constructor(private _http: Http) {}

  createRolelist(rolelist) {
    return this._http
      .post("/rolelist", rolelist)
      .map(data => data.json())
      .toPromise();
  }
  getRolelist(rolelist) {
    return this._http
      .get("/rolelist", rolelist)
      .map(data => data.json())
      .toPromise();
  }
  updateRolelist(rolelist) {
    return this._http
      .patch(`/rolelist/${rolelist._id}`, rolelist)
      .map(data => data.json())
      .toPromise();
  }

  destroyDistrict(id: string) {
    return this._http
      .delete(`/rolelist/${id}`)
      .map(data => data.json())
      .toPromise();
  }
}
